#HillClimbing과 Problem에 사용되는 부모 클래스 Setup 정의
class Setup:
    # delta, alpha, dx와 같은 설정들 initializing.
    def __init__(self) -> None:
        self._delta = 0.01
        self._alpha = 0.01
        self._dx = 0.0001