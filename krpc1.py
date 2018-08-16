import krpc
import time
import datetime

temp = 0
phase = 'Pre Launch'

start_time = time.time()
seconds_elapsed = 0

conn = krpc.connect(name='Hello World')
vessel = conn.space_center.active_vessel


def readout():
    print('')
    print(phase + ' ' + str(datetime.datetime.now()))
    print('seconds elapsed=' + str(seconds_elapsed))
    print('fuel_amount=' + str(fuel_amount))
    print('g-force=' + str(g_force))
    print('mean_altitude=' + str(mean_altitude))
    print('surface_altitude=' + str(surface_altitude))
    print('elevation=' + str(elevation))
    print('latitude=' + str(latitude))
    print('longitude=' + str(longitude))
    print('velocity=' + str(velocity))
    print('speed=' + str(speed))
    print('horizontal_speed=' + str(horizontal_speed))
    print('vertical_speed=' + str(vertical_speed))
    print('center_of_mass=' + str(center_of_mass))
    print('rotation=' + str(rotation))
    print('direction=' + str(direction))
    print('pitch=' + str(pitch))
    print('heading=' + str(heading))
    print('roll=' + str(roll))
    print('prograde=' + str(prograde))
    print('retrograde=' + str(retrograde))
    print('atmosphere_density=' + str(atmosphere_density))
    print('lift=' + str(lift))
    print('drag=' + str(drag))



print(vessel.name)

vessel.auto_pilot.target_pitch_and_heading(90, 90)
vessel.auto_pilot.engage()
vessel.control.throttle = 1
time.sleep(1)

phase = 'First Stage Burn'
print(phase)
vessel.control.activate_next_stage()
readout_displayed = 0

while True:

    seconds_elapsed=time.time()-start_time
    fuel_amount = vessel.resources.amount('LiquidFuel')
    g_force = vessel.flight().g_force
    mean_altitude = vessel.flight().mean_altitude
    surface_altitude = vessel.flight().surface_altitude
    elevation = vessel.flight().elevation
    latitude = vessel.flight().latitude
    longitude = vessel.flight().longitude
    velocity = vessel.flight().velocity
    speed = vessel.flight().speed
    horizontal_speed = vessel.flight().horizontal_speed
    vertical_speed = vessel.flight().vertical_speed
    center_of_mass = vessel.flight().center_of_mass
    rotation = vessel.flight().rotation
    direction = vessel.flight().direction
    pitch = vessel.flight().pitch
    heading = vessel.flight().heading
    roll = vessel.flight().roll
    prograde = vessel.flight().prograde
    retrograde = vessel.flight().retrograde
    atmosphere_density = vessel.flight().atmosphere_density
    lift = vessel.flight().lift
    drag = vessel.flight().drag


    if int(seconds_elapsed)%5 == 0 and int(seconds_elapsed) != readout_displayed:
        readout()
        readout_displayed = int(seconds_elapsed)

    #if vessel.flight(vessel.orbit.body.reference_frame).vertical_speed > 0:
       #print()

    if fuel_amount == 0.0 and temp == 0:
        phase = 'Main engine cutoff'
        print(phase)
        time.sleep(10)
        vessel.control.activate_next_stage()
        temp = 1
        phase = 'Descent Module'

    if temp == 1 and surface_altitude < 3000:
        vessel.control.activate_next_stage()
        phase = 'Drag Descent'
        temp = 2

    if heading != 90 or pitch != 90:
        vessel.auto_pilot.target_pitch_and_heading(90, 90)


