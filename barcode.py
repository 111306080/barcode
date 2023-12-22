import cv2
from pyzbar.pyzbar import decode
import time  # 引入時間模塊

def main():
    # 開啟攝像頭
    cap = cv2.VideoCapture(1)

    # 設定上一次條碼檢測的時間
    last_detection_time = 0

    while True:
        # 讀取攝像頭畫面
        ret, frame = cap.read()
        if not ret:
            print("Cannot receive frame. Exiting...")
            break

        # 轉換為灰階
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 解析條碼
        barcodes = decode(gray)

        # 檢查是否檢測到條碼並且距離上一次檢測的時間超過一定間隔（例如2秒）
        current_time = time.time()
        if barcodes and current_time - last_detection_time > 2:
            # 顯示解析結果
            for barcode in barcodes:
                barcode_data = barcode.data.decode("utf-8")
                barcode_type = barcode.type
                print(f"Detected Barcode: {barcode_data} (Type: {barcode_type})")

            # 更新上一次條碼檢測的時間
            last_detection_time = current_time

        # 顯示攝像頭畫面
        cv2.imshow('Camera', frame)

        # 按 'q' 鍵退出迴圈
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 釋放攝像頭並關閉視窗
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
