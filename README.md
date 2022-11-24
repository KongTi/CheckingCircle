# CheckingCircle
### CoinMarket에서 사용될 동전 검출기 제작 &rarr; 데이터 전처리 용이

- #### Hough Transform을 통해서 사진의 edge를 검출하고 Box를 보여준다
***
### 기본적인 실행 방법
`python run.py -fo <사진들이 있는 폴더> -fi <파일>`

- **예시**: `python run.py -fo sample/101/` &rarr; 폴더안의 모든 사진을 loading
   
- 지정된 폴더 (파일인 경우 파일이 있는 경로)에 **cooTXT, trash** 폴더가 생성된다   

  **cooTXT: 검출된 Box의 좌표 (YOLOv5모델 데이터)**   
  **trash: 버려지는 파일**

### 동작키

- #### D: 지정된 파일을 삭제 (trash폴더로 보낸다)
- #### Enter: Box좌표 저장 및 다음 사진으로 이동

### 하이퍼 파라미터

- #### blur: 가우시안 블러 적용 / 즉, 사진이 흐려짐 &rarr; 흐려질수록 동전안의 모양에 둔감해짐
  `값이 높을수록 블러 강도가 높음`
- #### dp: 해상도 반비례율 / 10-12추천
  `값이 높을수록 검출에 오류가 생김`
- #### minDist: 검출된 중심 사이의 거리 &rarr; 값 이하 거리에 있는 point는 검출하지 않는다
  `이미지 사이즈에 따라서 조절`
- #### cany_max: 경사도 누적 경계 값
  `값이 낮을수록 부정확한 검출값이 높아짐 / 즉, 일반화가 제대로 안됨`
- #### resize: 파일의 사이즈 조절
  `10이 원본 크기이며 1이 0.1배를 나타냄`

![example](https://github.com/KongTi/CheckingCircle/blob/main/example.PNG)
