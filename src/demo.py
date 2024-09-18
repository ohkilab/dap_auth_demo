from sampling.data_sampler import PairDataSampler, SamplingMode

import faulthandler
import tracemalloc


def sampling(user1_name, user2_name, device1_address, device2_address):

    sampler = PairDataSampler(
        user1_name,
        user2_name,
        device1_address,
        device2_address,
        mode=SamplingMode.DEMO,
    )
    sampler.run()
    device1_data, device2_data = sampler.get_data()
    device1_data.to_csv(f"{user1_name}.csv")
    device2_data.to_csv(f"{user2_name}.csv")
    return device1_data, device2_data


def main():
    print("plese input user1_name: ", end="")
    user1_name = input()
    print("plese input user2_name: ", end="")
    user2_name = input()
    # black band
    device1_address = "A59901F2-0211-6282-AA8C-4858238B4AE0"
    # blue band
    device2_address = "F76B7A81-43CD-5515-B7C3-997B6847F307"

    device1_data, device2_data = sampling(
        user1_name,
        user2_name,
        device1_address,
        device2_address,
    )


if __name__ == "__main__":

    tracemalloc.start()
    faulthandler.enable()

    main()

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics("traceback")

    print("[ Top 10 ]")
    for stat in top_stats[:10]:
        print(stat)
        for line in stat.traceback.format():
            print(line)
        print("=====")