def main():
    """
    ##################################################
    Comlete your code here
    Use m_perc and f_perc for your results
    ##################################################
    """
    mNum = int(input('Enter the number of male students: '))
    fNum = int(input ('Enter the number of female students: '))
    total = fNum + mNum
    m_perc = mNum / total * 100
    f_perc = fNum / total * 100
    print(f'The percentage of male students is {m_perc:.2f}')
    print(f'The percentage of female students is {f_perc:.2f}')
    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    return m_perc, f_perc


if __name__ == '__main__':
    main()
