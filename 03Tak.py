def Vibration_Distance():
    v = float(input("กรุณากรอกความเร็ว: "))  # Input speed (v)
    f = float(input("กรุณากรอกความเร็วรอบ: "))  # Input frequency (f)
    
    D = 27010 * v * f
    
    print(f"ระยะการสั่นสะเทือน: {D} mm")

    if D < 1.80:
        print("เหมาะสำหรับเครื่องจักรขนาดกลางลงมา")
    elif D > 1.80:
        print("เหมาะสำหรับเครื่องจักรขนาดใหญ่ขึ้นไป")
        
Vibration_Distance()
