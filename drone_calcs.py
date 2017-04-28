def pres_alt_calc(qnh, air_elev):
    if qnh >= 1013.25:
        qnh = int(qnh) - 1013.25
        qnh = qnh * 30
        pres_alt = int(air_elev) - qnh

    else:
        qnh = int(qnh) + 1013.25
        qnh = qnh * 30
        pres_alt = int(air_elev) - qnh

    return pres_alt


def den_alt_calc(temp, qnh, air_elev):
    original_pres_alt = pres_alt_calc(qnh, air_elev)

    pres_alt = original_pres_alt * -0.002

    pres_alt = pres_alt + 15

    temp = temp - pres_alt

    temp = temp * 120

    answer = original_pres_alt + temp

    return answer
