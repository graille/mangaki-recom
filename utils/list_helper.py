class ListHelper:
    @staticmethod
    def intersect(a, b):
        # from 642763
        return list(set(a) & set(b))