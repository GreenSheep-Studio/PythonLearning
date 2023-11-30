def main():
    x = input()
    try:
        x = float(x)
        if x > 0 and x<= 19:
            print(f"应缴水费：{(x*3.35):.3f}，其中：自来水费：{(x*2.40):.3f}，污水处理费：{(x*0.95):.3f}。")
        elif x > 19 and x <= 30:
            x = x - 19
            zAll = 19 * 3.35
            zZi = 19 * 2.40
            zWu = 19 * 0.95
            print(f"应缴水费：{(x*4.55 + zAll):.3f}，其中：自来水费：{(x*3.60 + zZi):.3f}，污水处理费：{(x*0.95 + zWu):.3f}。")
        elif x > 30:
            x = x - 30
            zAll = 19 * 3.35 + 11 * 4.55
            zZi = 19 * 2.40 + 11 * 3.60
            zWu = 19 * 0.95 + 11 * 0.95
            print(f"应缴水费：{(x*8.15):.3f}，其中：自来水费：{(x*7.20):.3f}，污水处理费：{(x*0.95):.3f}。")
        else:
             print("输入错误!")
    except ValueError:
        print("输入错误!")

if __name__ == "__main__":
        main()