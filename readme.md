# 2023 2-2 Project (23.10 ~ ing)
---

## NyangNyang torch
---

![스크린샷 2023-12-17 오후 9.25.42.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/35860b6c-2d3d-4a76-9237-ed427ebe063a/307653ff-0d1d-4597-8d53-26360c54aec7/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2023-12-17_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_9.25.42.png)

### 1) 선정 동기

Deep Learning 을 공부하고 Project 와 다양한 competition 에 참가해보면서 많은 실험을 진행해보았다. 하지만 문제의 본질을 파악하고 내부의 원리를
이해한 후 문제를 해결해야 하지만 단순히 성능(수치)를 높이기 위해,
competition 에서 조금이라도 높은 리더보드 순위를 얻기 위해 기계적으로
실험을 돌리는 경우가 많았다. 또한 DeepLearning Framwork(Pytorch)를
사용하면서 그 내부 동작 원리에 대한 의문이 드는 경우가 많았으며 그것은
실제로 많은 사람들이 하는 의문이기도 하다. DeepLearning 분야의 대학원
진학을 희망하는 현재 상황에서 또 다른 task 에 관심을 갖고 공부하기 보다는
머리 속의 Deep Learning flow 에 대한 정리와 놓치고 지나갔던 부분의 공부가
필요하다고 느꼈으며 이러한 시간을 바탕으로 3 학년 때는 좀 더 advance 된
task 를 진행하고 싶었다. 그래서 2-2 때에는 이런 욕구를 충족시킬 수 있는
“나만의 DeepLearning Framework 제작”에 관심을 갖게 되었다.

결국 “냥냥 torch”라는 새로운 Deep Learning framework 를 직접 제작해 보기로
하였으며 “냥냥 torch”를 개발하는 과정을 통해 이러한 이점을 얻을 수 있을
것이라고 생각했다.
1. data, model, loss, optimizer, train, inference 에 이르는 부분을 구현해야 하니
Deep Learning 학습 과정에 대한 전반적인 이해도를 높일 수 있다.

2. 현대 프로그래밍에 필수적인 OOP(Object-Oriented Programming)를 연습할
수 있다.
3. 모든 과정을 직접 구현하기 때문에 Implementation 능력을 향상시킬 수 있다.

또한 현재 가장 널리 쓰이고 있는 Pytorch 의 방식을 일부 reference 하여
Pytorch Framework 자체의 이해도도 늘릴 수 있을 것으로 예상한다.
현재 Pytorch 를 비롯한 많은 Framework 들은 다양한 Task 에 활용할 수 있지만
“냥냥 torch”는 Classification Task 에 대해서만 사용할 수 있다. 그 이유 중
첫번째는 물리적인 구현시간에 한계가 있을 것이라고 생각했다. 두번째는 다른
framework 처럼 거대한 프로젝트를 혼자 진행하기에는 구현능력이 부족하다고
생각했다. 또한 “냥냥 torch”의 학습속도나 성능 등이 아직 미지수이기 때문에
먼저 비교적 간단한 Task 부터 수행할 수 있게 프로젝트의 방향을 설정하였다.
또한 이번 “냥냥 torch”의 구현이 성공적으로 끝난다면 추가적인 Task 에 대한
기능을 추가해 update 하는 방식으로 진행하고자 한다.

프로젝트 세부 계획은 [냥냥torch pdf](냥냥torch(docx).pdf) 참고
