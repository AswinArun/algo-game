import math
import random

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Radius of the ball
BALL_RADIUS = 20

# Maximum power that can be used to shoot
MAX_POWER = 30

# Friction factor applied to the ball's movement to simulate deceleration
FRICTION = 0.995

# Speed of the bullet when fired
BULLET_SPEED = 15

def player_script(cannon_pos, ball_pos, power_bullet_count, precision_bullet_count, ball_vel):
    """
    Determines the angle, power, and bullet type for shooting the ball.
    
    Parameters:
    cannon_pos: tuple
        Coordinates (x, y) of the cannon.
    ball_pos: tuple
        Coordinates (x, y) of the ball (target position).
    power_bullet_count: int
        Number of power bullets remaining.
    precision_bullet_count: int
        Number of precision bullets remaining.
    ball_vel: tuple
        Current velocity of the ball as (vx, vy).
        
    Returns:
    tuple or None
        (angle, power, bullet_type) for the shot, or None if no shot is made.
        - angle: The angle in degrees to aim the cannon.
        - power: The power level for the shot (1 to MAX_POWER).
        - bullet_type: The type of bullet ("power" or "precision").
    """
    # Unpack cannon position
    cannon_x, cannon_y = cannon_pos

    # Define the target position
    target_x, target_y = ball_pos
    power=0
    # Placeholder logic to calculate shooting parameters
    not_shooting = False  # Set to True if the cannon chooses not to shoot
    if(cannon_x<WIDTH/2):
        angle = random.uniform(-90, 90)  # Random angle to shoot in
    else:
        
      power = 30*((((800-target_x)**2+(600-target_y)**2)**(.5))/((800*800+600*600)**(.5) )) 
    if(((800-target_x)**2+(600-target_y)**2)**(.5))<=(((800*800+600*600)**(.5) )/2):
     bullet_type="power"
    else :
       bullet_type="precision"
    
    Y=target_y + ball_vel(0)*power - cannon_y
    X=target_x + ball_vel(1)*power - cannon_x
    angle = math.degree(math.atan(Y,X))
    # Decide whether to shoot or not
    if not_shooting:
        return None  # Do not shoot

    # Return the shooting parameters
    return (angle, power, bullet_type)
