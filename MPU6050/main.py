from machine import Pin, I2C #needed for set the pins
import mp_mpu6050.mp_mpu6050 as mpu_lib #mpu6050 library
import time

mpu = mpu_lib.MPU6050() #set MPU6050 module

while True:
    gyro = mpu.read_gyro_data() #read the gyro data
    gyroX = gyro["x"] #gyro data X
    gyroY = gyro["y"] #gyro data Y
    gyroZ = gyro["z"] #gyro data Z

    accel = mpu.read_accel_data() #read the accelometer data
    accelX = accel["x"] #accelometer data X
    accelY = accel["y"] #accelometer data y
    accelZ = accel["z"] #accelometer data Z


    print(f"Gyro X: {str(round(gyroX, 2))}, Gyro Y: {str(round(gyroY, 2))}, Gyro Z: {str(round(gyroZ, 2))}") #print the gyro data, in string, rounded
    print(f"Accel X: {str(round(accelX, 2))}, Accel Y: {str(round(accelY, 2))}, Accel Z: {str(round(accelZ, 2))}") #print the accelometer data, in string, rounded

    time.sleep(0.5)
