class TestExample:
    def test_check_math(self):
        a=5
        b=9
        assert a+b==14
    def test_check_math2(self):
        a=5
        b=9
        ex_summ=15
        assert a+b==ex_summ, f"Sum of variable not equel to {ex_summ}"

