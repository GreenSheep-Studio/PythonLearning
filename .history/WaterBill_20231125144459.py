def main():
    x = input()
    try:
        x = float(x)
        if x > 0 and x<= 19:
            print(f"应缴水费：{(x*3.35):.3f}，其中：自来水费：{(x*2.40):.3f}，污水处理费：{(x*0.95):.3f}")
        elif x > 19 and x <= 30:
            print(f"应缴水费：{(x*4.55):.3f}，其中：自来水费：{(x*3.60):.3f}，污水处理费：{(x*0.95):.3f}")
        elif x > 30:
            print(f"应缴水费：{(x*8.15):.3f}，其中：自来水费：{(x*27.20):.3f}，污水处理费：{(x*0.95):.3f}")
    except ValueError:
        print("输入错误!")

if __name__ == "__main__":
        main()