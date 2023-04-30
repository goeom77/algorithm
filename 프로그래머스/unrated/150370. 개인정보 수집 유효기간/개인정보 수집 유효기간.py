def solution(today, terms, privacies):
    t_year, t_month, t_day = map(int, today.split("."))
    t_date = t_year*12 + t_month
    duration = {}
    for term in terms:
        name, date = term.split()
        duration[name] = int(date)
    answer = []
    tmp = 1
    for privacy in privacies:
        date, m_term = privacy.split()
        m_year, m_month, m_day = map(int, date.split("."))
        m_date = m_year*12 + m_month + duration[m_term]
        if m_date < t_date:
            answer.append(tmp)
        elif m_date == t_date and m_day <= t_day:
            answer.append(tmp)
        tmp += 1
    return answer