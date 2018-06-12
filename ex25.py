print("Let's practice everything.")
print('You\'d need to know \'but escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and repuires an explanation
\n\t\twhere there is none.
"""

print("------------")
print(poem)
print("-----------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formuls(started):
    jelly_beans = started * 500
    jars = jelly_beans / 10000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 1000
beans, jars, crates = secret_formula(start_point)

#remember that this is another way to format a string
