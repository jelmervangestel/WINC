# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
def greet(name, greeting="Hello, <name>"):
    ans = greeting.replace("<name>", name)
    return ans

def force(mass, body):
    bodies = {'Sun'     : 274,
              'Jupiter' : 24.9,
              'Neptune' : 11.2,
              'Saturn'  : 10.4,
              'Earth'   : 9.8,
              'Uranus'  : 8.87,
              'Venus'   : 8.9,
              'Mars'    : 3.7,
              'Mercury' : 3.7,
              'Moon'    : 1.6,
              'Pluto'   : 0.6}

    return mass*bodies[body]

def pull(m1, m2, d):
    G = 6.674*(10**-11)
    return G * ((m1*m2)/(d**2))