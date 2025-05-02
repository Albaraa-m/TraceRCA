from hotelreservation_config import INVOLVED_SERVICES


def simple_name(full_name):
    ret = full_name.split('_')[0]
    assert ret in INVOLVED_SERVICES, f"full={full_name}, ret={ret}"
    return ret
    # if 'istio-ingressgateway' in full_name:
    #     return 'gateway'
    # full_name = full_name.split('.')[0]
    # ret_list = []
    # ok = False
    # for part in full_name.split("-"):
    #     if part == "ts":
    #         ok = True
    #     elif "service" in part:
    #         ok = False
    #         break
    #     elif ok:
    #         ret_list.append(part)
    # if len(ret_list) <= 0:
    #     ret = full_name
    # else:
    #     ret = "-".join(ret_list)
    # assert ret in INVOLVED_SERVICES, f"full={full_name}, ret_list={ret_list}"
    # return ret
