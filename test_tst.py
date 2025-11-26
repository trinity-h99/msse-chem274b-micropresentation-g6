from tst import TST


class TestTST:
    """
    To run:
    pytest test_tst.py
    """
    def _create_tst(self, word_list):
        tst = TST()
        for i, word in enumerate(word_list):
            tst.put(word, i + 1)  # TODO: what should the value be?
        return tst

    def test_adds_sequences_correctly(self):
        sequences = ['AABHSNK', 'WNHJJJE', 'EPJKKSK', 'EPJKKSKSS', 'EPJKKSA']
        tst = self._create_tst(sequences)
        assert tst.contains('EPJKKSK') == True
        assert tst.contains('EPJKKSKSS') == True
        assert tst.contains('EPJKKSKSL') == False
        assert tst.get('EPJKKSKSS') == 4    
