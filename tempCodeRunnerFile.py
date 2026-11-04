def calc_oee(equipment):
    availability = (
        equipment["uptime"]
        /
        (
            equipment["uptime"]
            + equipment["downtime"]
        )
    )
    quality = (
        equipment["production"]
        - equipment["defect"]
    ) / equipment["production"]
    oee = availability * quality
    return oee