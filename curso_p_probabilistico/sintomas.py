
def calc_bayes(priorA, prob_B_dado_A, prob_B): #prob_A_dado_B
    return (priorA * prob_B_dado_A)/prob_B


if __name__== '__main__':
    #Esta información viene de datos de Aroesti
    prob_cancer = 1/100000
    prob_sintoma_dado_cancer = 1
    prob_sintoma_dado_no_cancer = 10/99999
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    prob_cancer_dado_sintoma = calc_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(prob_cancer_dado_sintoma)

