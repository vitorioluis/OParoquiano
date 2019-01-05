package br.com.oparoquiano.app.Dominio.Entidades;

/**
 * Created by luis on 19/06/17.
 */

public class Pontuacao {
    public static String nomeTabela = "tb_pontuacao";

    private String pon_tabela;
    private String pon_id_tabela;
    private int pon_pontos;

    public String getPon_tabela() {
        return pon_tabela;
    }

    public void setPon_tabela(String pon_tabela) {
        this.pon_tabela = pon_tabela;
    }

    public String getPon_id_tabela() {
        return pon_id_tabela;
    }

    public void setPon_id_tabela(String pon_id_tabela) {
        this.pon_id_tabela = pon_id_tabela;
    }

    public int getPon_pontos() {
        return pon_pontos;
    }

    public void setPon_pontos(int pon_pontos) {
        this.pon_pontos = pon_pontos;
    }
}
