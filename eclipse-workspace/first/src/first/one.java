package first;

public class one {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int itemA = 10;
		int itemB = 50;
		int itemC = 100;
		double totalprice = itemA + itemB + itemC;
		double disprice = totalprice - (0.1*totalprice);
		double amountpayable = disprice + (0.05*disprice);
		System.out.println("Net amount paid by John : Rs" + amountpayable);

	}

}
