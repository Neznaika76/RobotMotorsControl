# motots_control.py
def move_motor(speed):
    print(f"Motor moving at speed {speed}")

if __name__ == "__main__":
    move_motor(50)
    
import time

def set_speed(motor_id, speed):
    # Симуляция установки скорости двигателя
    print(f"Setting motor {motor_id} to speed {speed}")

def smooth_acceleration(motor_id, start_speed, end_speed, duration):
    step = (end_speed - start_speed) / duration
    current_speed = start_speed
    
    for _ in range(duration):
        set_speed(motor_id, int(current_speed))
        current_speed += step
        time.sleep(1)

def handle_user_input():
    while True:
        try:
            command = input("Enter a command (set/smooth/exit): ").strip().lower()
            if command == 'set':
                motor_id = int(input("Motor ID: "))
                speed = int(input("Speed: "))
                set_speed(motor_id, speed)
            elif command == 'smooth':
                motor_id = int(input("Motor ID: "))
                start_speed = int(input("Start Speed: "))
                end_speed = int(input("End Speed: "))
                duration = int(input("Duration (seconds): "))
                smooth_acceleration(motor_id, start_speed, end_speed, duration)
            elif command == 'exit':
                break
            else:
                print("Invalid command")
        except ValueError:
            print("Please enter valid integer values.")

if __name__ == "__main__":
    handle_user_input()

def smooth_deceleration(motor_id, start_speed, end_speed, duration):
    step = (start_speed - end_speed) / duration
    current_speed = start_speed
    
    for _ in range(duration):
        set_speed(motor_id, int(current_speed))
        current_speed -= step
        time.sleep(1)
