from math import sqrt


class MathHelper:
    @staticmethod
    def geometricMean(numbers):
        product = 1
        for n in numbers:
            product *= n
        return product ** (1.0 / len(numbers))

    @staticmethod
    def arithmeticMean(numbers):
        return float(sum(numbers)) / max(len(numbers), 1)

    @staticmethod
    # Defined here : https://en.wikipedia.org/wiki/Pearson_correlation_coefficient#For_a_sample
    def pearson_correlation_coefficient(sample1, sample2):
        assert len(sample1) == len(sample2)
        n = len(sample1)

        if n == 0:
            return -1

        meanS1, meanS2 = MathHelper.arithmeticMean(sample1), MathHelper.arithmeticMean(sample2)
        sumS1Sq, sumS2Sq = sum([pow(x, 2) for x in sample1]), sum([pow(x, 2) for x in sample2])
        sumS1S2 = sum([sample1[i] * sample2[i] for i in range(n)])

        try:
            return (sumS1S2 - n * meanS1 * meanS2) / (
                sqrt(sumS1Sq - n * pow(meanS1, 2)) * sqrt(sumS2Sq - n * pow(meanS2, 2)))
        except ZeroDivisionError:
            return 0
