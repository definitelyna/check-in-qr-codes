import qrcode

for i in range(1, 401):
    img=qrcode.make(f"checkinattendee{i}")
    img.save(f"checkinattendee{i}.png")