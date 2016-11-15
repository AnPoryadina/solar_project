# coding: utf-8
# license: GPLv3

gravitational_constant = 6.67408E-11


def calculate_force(body, space_objects):

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += gravitational_constant*obj.m*body.m/((body.x - obj.x)**2)
        body.Fy += gravitational_constant*obj.m*body.m/((body.y - obj.y)**2)


def move_space_object(body, dt):

    ax = body.Fx/body.m
    body.x += body.x + body.Vx*dt + ax*(dt**2)/2
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y += body.y + body.Vy*dt + ay*(dt**2)/2
    body.Vy += ay*dt


def recalculate_space_objects_positions(space_objects, dt):

    for body in space_objects:
        calculate_force(body, space_objects)

    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
