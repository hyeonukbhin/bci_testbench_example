# BCI Testbench Example

BCI 모듈 자체 테스트를 위한 테스트 벤치 예제 저장소

## 1. Description

- ROS
- Ubuntu

## 2. Requirements

```bash
sudo pip install -r requiremets.txt
```

## 3. Usage

### Input Talker 실행

```bash
rosrun bci_testbench_example input_talker.py
```

실행 후 기입한 숫자로부터 1씩 줄어드는 토픽 발행됩니다.
토픽 이름과 메세지 타입 변경해서 사용하세요.

### Output Listener 실행

```bash
rosrun bci_testbench_example output_listener.py
```

실제 BCI 에서 나오는 토픽으로 변경해서 사용하세요

### Rosbag Record Shell 스크립트 실행

```bash
./scripts/rosbag_record.sh
```

파일을 열어서 record 하려는 토픽 이름들을 뒤에 인자로 수정해서 사용하세요.
