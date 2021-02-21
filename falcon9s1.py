
import math

## Simulate flight of first stage of the Falcon 9 (FT) rocket to
## find out how high it can go

## an answer(?): 
# https://www.reddit.com/r/spacex/comments/5tklb4/falcon_9ft_first_stage_flight_analysis/

## From SpaceX web page:
takeoff_weight = 549054.0     # kg
stage1_burn_time = 162        # s
stage1_thrust_sl = 7607000.0  # N (kg m / s^2)
stage1_thrust_vac = 8227000.0 # N (kg m / s^2)

## https://space.stackexchange.com/questions/17945/falcon-9-fuel-use
# "Mass of propellant on first stage, fuel + oxidizer, is on the order
#  of 395,700kg"
stage1_fuel = 395700.0        # kg

burn_rate = stage1_fuel / stage1_burn_time # assuming this is constant...

stage1_burn_rate = stage1_fuel / stage1_burn_time  # kg / s
non_fuel_weight = takeoff_weight - stage1_fuel

gravity = 9.81  # m / s^2

def thrust(altitude, thrust_at_sea_level, thrust_in_vacuum):
    '''Calculate thrust as a function of altitude, using the given
    values for thrust at sea level and in vacuum. We assume a linear
    interpolation, and that vacuum begins at 120km (100-120km seems
    a reasonable guess; see
    https://en.wikipedia.org/wiki/Atmosphere_of_Earth).'''
    if altitude < 120000:
        f = altitude / 120000
        return (f * (thrust_in_vacuum - thrust_at_sea_level)) + thrust_at_sea_level
    else:
        return thrust_in_vacuum

# The variables that we will be keeping track of in the simulation:
altitude = 0
velocity = 0
mass = takeoff_weight
time = 0

delta_t = 1 # in seconds

# The stop condition here is just that time has reached the end of
# stage 1 burn time. Alternatively, we could stop the loop when the
# remaining fuel is zero (or just less than what would be consumed
# during the next delta_t time interval); however, to do that we
# would also need to track fuel separately from mass.
file = open("E:\\comp6730\\lab8\\falcon.csv", "r+")
print("file being written")
files = file.readlines()
words = files[-1].split(',')
time = int(words[1])
velocity = float(words[3])
altitude = float(words[5])
mass = float(words[7])
while time < stage1_burn_time:
    # Calculate update simulation variables based on current values:
    
    altitude = altitude + (velocity * delta_t)
    acceleration = (thrust(altitude, stage1_thrust_sl, stage1_thrust_vac) / mass) - gravity
    velocity = velocity + (acceleration * delta_t)
    mass = mass - burn_rate * delta_t
    time = time + delta_t
    # Print the state
    file.seek(2)
    file.write("\ntime:,")
    file.write(str(time))
    file.write(",velocity:,")
    file.write(str(velocity))
    file.write(",altitude:,")
    file.write(str(altitude))
    file.write(",mass:,")
    file.write(str(mass))
file.close()
    # The is following is a more advanced use of printing which produces
    # a more nicely formatted output. To use it, comment the print call
    # above and uncomment this instead.
    #print("time: {}s, velocity: {:.2f}m/s, altitude: {:.2f}km, mass: {:.0f}kg".format(time, velocity, altitude/1000, mass))
