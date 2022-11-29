import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static int rec(int num){
        if (num == 0) {
            // When method gets 0, just return 1.
            return 1;
        } else {

            return num * rec(num - 1);
        }
    }

    public static void zad1a(String[] args) {
        int wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();

        for (int i = 1; i <=num; i++){
            System.out.println("Podaj liczbe: ");
            int dod = n.nextInt();
            wynik += dod;
        }
        System.out.println("\n Suma liczb to " + wynik);
    }

    public static void zad1b(String[] args){
        int wynik = 1;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();

        for (int i = 1; i <=num; i++){
            System.out.println("Podaj liczbe: ");
            int mno = n.nextInt();
            wynik *= mno;
        }
        System.out.println("\n wynik to " + wynik);
    }
    public static void zad1c(String[] args){
        int wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();

        for(int i = 1; i <=num; i++){
            System.out.println("podaj liczbe: ");
            wynik += Math.abs(n.nextInt());

        }
        System.out.println("wynik to: "+ wynik);
    }

    public static void zad1d(String[] args){
        int wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();

        for(int i = 1; i <=num; i++){
            System.out.println("podaj liczbe: ");
            wynik += Math.sqrt(Math.abs(n.nextInt()));

        }
        System.out.println("wynik to: "+ wynik);
    }

    public static void zad1e(String[] args){
        int wynik = 1;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();

        for(int i = 1; i <=num; i++){
            System.out.println("podaj liczbe: ");
            wynik *= Math.abs(n.nextInt());

        }
        System.out.println("wynik to: "+ wynik);
    }

    public static void zad1f(String[] args){
        int wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();

        for(int i = 1; i <=num; i++){
            System.out.println("podaj liczbe: ");
            wynik += Math.pow(n.nextInt(),2);

        }
        System.out.println("wynik to: "+ wynik);
    }
    public static void zad1g(String[] args){
        int wynik = 0;
        int wynik1 = 1;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();
        int k;

        for(int i = 1; i <=num; i++){

            System.out.println("podaj liczbe: ");
            k = n.nextInt();
            wynik += k;
            wynik1 *= k;

        }
        System.out.println("wynik dodawania to: "+ wynik +" wynik mnozenia to: "+ wynik1);
    }
    public static void zad1h(String[] args){
        int wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();
        for(int i = 1; i <=num; i++){
            System.out.println("podaj liczbe: ");
            wynik += n.nextInt()+Math.pow((-1),i-1);

        }
        System.out.println("wynik to: "+ wynik);

    }
    public static void main(String[] args){
        float wynik = 0;

        Scanner n = new Scanner(System.in);
        System.out.println("Podaj n: ");
        int num = n.nextInt();
        for(int i = 0; i <num; i++){
            System.out.println("podaj liczbe: ");
            wynik += n.nextInt() * Math.pow((-1),i+1) / rec(i+1);

        }
        System.out.println("wynik to: "+ wynik);

    }
}
