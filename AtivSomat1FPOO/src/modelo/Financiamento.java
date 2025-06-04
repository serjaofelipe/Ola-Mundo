package modelo;

public record Financiamento(double valorImovel, int prazoFinanciamentoAnos, double taxaJurosAnual) {
    public double calcularPagamentoMensal() {
        int numeroDeMeses = this.prazoFinanciamentoAnos * 12;
        double taxaDeJurosMensal = this.taxaJurosAnual / 12;
        return (this.valorImovel / numeroDeMeses) * (1 + taxaDeJurosMensal);
    }
    public double calcularTotalPagamento() {
        return calcularPagamentoMensal() * this.prazoFinanciamentoAnos * 12;
    }

    public void mostrarDadosFinanciamento() {

        System.out.printf(" // Valor do Imóvel: R$ %.2f || ", valorImovel());
        System.out.printf(" Prazo do Financiamento: %d anos || ", prazoFinanciamentoAnos());
        System.out.printf(" Taxa de Juros Anual: %.1f%% || ", taxaJurosAnual() * 100);
        System.out.printf(" Pagamento Mensal: R$ %.2f || ", calcularPagamentoMensal());
        System.out.printf(" Valor do Financiamento: R$ %.2f. // \n", calcularTotalPagamento());
    }
}