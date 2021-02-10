# 特徴点マッチング

## 特徴点検出器

- AKAZE特徴量

    ```
    type = cv2.AKAZE_create()
    ```

- BRISK特徴量
- KAZE特徴量
- ORB特徴量

## マッチング器

- 特徴点検出及び特徴量記述子の計算

    ```
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    ```

- cv2.BFMatcher：総当たりによるマッチング
  
    ```
    kp1, desc1 = type.detectAndCompute(tmp, None)
    kp2, desc2 = type.detectAndCompute(img, None)
    ```

- 最近傍マッチング

    ```
    matches = bf.match(desc1, desc2)
    ```

- k近傍法マッチング

    ```
    matches = bf.knnMatch(desc1, desc2, k=2)
    ```
    
    - テンプレート(tmp)のある特徴点と1番目，2番目に距離が近い対象画像(img)の特徴点を探索

- レシオテスト(resio test)
  - 1番目に近い距離と2番目に近い距離の差があまりない場合，信頼性に欠けるので除外
  $$ \dfrac{1番目に近い距離}{2番目に近い距離} < threshold $$