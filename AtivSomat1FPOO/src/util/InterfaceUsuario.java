package util;

import java.util.Scanner;
import java.util.InputMismatchException;

public class InterfaceUsuario {
    private final Scanner scanner;

    public InterfaceUsuario() {
        this.scanner = new Scanner(System.in);
    }

    public double valorImovel() {
        double valor = 0;
        boolean entradaValida = false;
        do {
            System.out.print("Digite o valor do imóvel: R$ ");
            try {
                valor = scanner.nextDouble();
                if (valor > 0) {
                    entradaValida = true;
                } else {
                    System.out.println("Erro: O valor do imóvel deve ser positivo. Tente novamente!\n ");
                }
            } catch (InputMismatchException e) {
                System.out.println("Erro: Entrada inválida. Digite um número (ex: 500000,00). Tente novamente!\n ");
                scanner.nextLine();
            }
        } while (!entradaValida);
        return valor;
    }

    public int prazoFinanciamentoAnos() {
        int prazo = 0;
        boolean entradaValida = false;
        do {
            System.out.print("Digite o prazo do financiamento (em anos inteiros): ");
            try {
                prazo = scanner.nextInt();
                if (prazo > 0) {
                    entradaValida = true;
                } else {
                    System.out.println("Erro: O prazo do financiamento deve ser em anos inteiros. Tente novamente!\n ");
                }
            } catch (InputMismatchException e) {
                System.out.println("Erro: Entrada inválida. Digite em anos inteiros (ex: 30). Tente novamente!\n ");
                scanner.nextLine();
            }
        } while (!entradaValida);
        return prazo;
    }

    public double taxaJurosAnual() {
        double taxa = 0;
        boolean entradaValida = false;
        do {
            System.out.print("Digite a taxa de juros anual (ex: 0,075 para 7.5%): ");
            try {
                taxa = scanner.nextDouble();
                if (taxa > 0 && taxa <= 1000.0) {
                    entradaValida = true;
                } else if (taxa <= 0) {
                    System.out.println("Erro: A taxa de juros anual deve ser um valor positivo. Tente novamente!\n ");
                } else {
                    System.out.println("Erro: A taxa de juros anual não pode ser maior que 1000 (100000%). Tente novamente!\n ");
                }
            } catch (InputMismatchException e) {
                System.out.println("Erro: Entrada inválida. Digite um número válido (ex: 0,075 para 7.5%). Tente novamente!\n ");
                scanner.nextLine();
            }
        } while (!entradaValida);
        return taxa;
    }
    public void fecharScanner() {
        this.scanner.close();
    }
}


