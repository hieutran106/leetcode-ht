class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = sorted(list(str(n)), reverse=True)
        num = int("".join(digits))

        power_2_arr = [1, 2, 4, 8, 61, 32, 64, 821, 652, 521, 4210, 8420, 9640, 9821, 86431, 87632, 66553, 732110, 644221, 885422, 8765410, 9752210, 9444310, 8888630, 77766211, 55443332, 88766410, 877432211, 866554432, 987653210, 8774432110, 8876444321, 9997664422, 9998855432]

        return num in power_2_arr
