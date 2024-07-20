import dis
import sys
import textwrap
import types
from io import StringIO

from byterun.pyvm import VirtualMachine, VirtualMachineError

def assert_same_exc(vm_exc, py_exc):
    """Exceptions don't implement __eq__, check it ourselves."""
    assert str(vm_exc) == str(py_exc), f"{vm_exc} != {py_exc}"
    assert type(vm_exc) == type(py_exc)

DEBUG = False
TEST_NAME = 'test'

def set_debug(v):
    global DEBUG
    DEBUG = v
def set_test_name(v):
    global TEST_NAME
    TEST_NAME = v

def assert_ok(code, raises=None, name=None, debug=None):
    """Run `code` in our VM and in real Python: they behave the same."""

    if name is None:
        name = TEST_NAME
    if debug is None:
        debug = DEBUG

    code = textwrap.dedent(code)
    code = compile(code, name, "exec", 0, 1)
    # Print the disassembly so we'll see it if the test fails.
    dis.dis(code)

    real_stdout = sys.stdout
    vm_stdout = StringIO()
    if not debug:
        sys.stdout = vm_stdout

    vm = VirtualMachine()
    vm_ret = vm_exc = None
    try:
        vm_ret = vm.run_code(code)
    except (VirtualMachineError, AssertionError):
        raise
    except Exception as e:
        if debug:
            raise
        vm_exc = e
    finally:
        real_stdout.write("--------vm: stdout start----------\n")
        real_stdout.write(vm_stdout.getvalue())
        real_stdout.write("--------vm: stdout end----------\n")

    py_stdout = StringIO()
    sys.stdout = py_stdout

    py_ret = py_exc = None
    gvars = {}
    try:
        py_ret = eval(code, gvars, gvars)
    except AssertionError:              # pragma: no cover
        raise
    except Exception as e:
        py_exc = e
    # finally:
    #     real_stdout.write("--------stdout from py----------\n")
    #     real_stdout.write(py_stdout.getvalue())

    sys.stdout = real_stdout

    assert_same_exc(vm_exc, py_exc)
    assert vm_ret == py_ret
    assert vm_stdout.getvalue() == py_stdout.getvalue()

    if raises:
        assert isinstance(vm_exc, raises)
    else:
        assert vm_exc is None


