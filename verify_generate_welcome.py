from pathlib import Path

source = Path('main.py').read_text()
start = source.index('def generate_welcome')
end = source.index('def generate_receipt')
func_src = source[start:end]
ns = {}
exec(func_src, ns)

assert ns['generate_welcome']('Urban Style', 100, False, True,
                              True) == 'Welcome to Urban Style! Your haircut costs $100.00.'
assert ns['generate_welcome']('Urban Style', 100, True, True,
                              False) == 'Welcome to Urban Style! Your haircut costs $80.00 with your first visit discount.'
assert ns['generate_welcome']('Urban Style', 100, True, False,
                              False) == 'Welcome back to Urban Style! Your haircut costs $85.00 with your frequent client discount.'
assert ns['generate_welcome']('Urban Style', 100, False, False,
                              False) == 'Welcome to Urban Style! Your haircut costs $100.00.'
assert ns['generate_welcome'](
    'Urban Style', 0, False, False, False) == 'Invalid price'
print('verified')
