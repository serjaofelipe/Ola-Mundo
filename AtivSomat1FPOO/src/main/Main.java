package main;

import modelo.Financiamento;
import util.InterfaceUsuario;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        InterfaceUsuario interfaceUsuario = new InterfaceUsuario();
        List<Financiamento> listaDeFinanciamento = new ArrayList<>();

        System.out.println("-------- Sistema de Financiamento Imobiliário --------\n");

        for (int i = 0; i < 4; i++) {
            System.out.println("Adicionando Financiamento #" + (i + 1));
            double valorImovel = interfaceUsuario.valorImovel();
            int prazoAnos = interfaceUsuario.prazoFinanciamentoAnos();
            double taxaJurosAnual = interfaceUsuario.taxaJurosAnual();

            listaDeFinanciamento.add(new Financiamento(valorImovel, prazoAnos, taxaJurosAnual));
            System.out.println("\nFinanciamento #" + (i + 1) + " adicionado com sucesso!\n");
        }

        System.out.println("\n-------- Lista completa de financiamentos --------");

        double totalValorImoveis = 0;
        double totalFinanciados = 0;

        for (int i = 0; i < listaDeFinanciamento.size(); i++) {
            Financiamento f = listaDeFinanciamento.get(i);
            System.out.println("\nFinanciamento #" + (i + 1) + ":");
            f.mostrarDadosFinanciamento();

            totalValorImoveis += f.valorImovel();
            totalFinanciados += f.calcularTotalPagamento();
        }

        System.out.printf("\nTotal de todos os imóveis: R$ %.2f || Total de todos os financiamentos: R$ %.2f\n", totalValorImoveis, totalFinanciados);
        System.out.println("\n-------- Fim da Lista --------\n");

        interfaceUsuario.fecharScanner();
        System.out.println("\n-------- Sistema de Financiamento Encerrado --------");
    }
}