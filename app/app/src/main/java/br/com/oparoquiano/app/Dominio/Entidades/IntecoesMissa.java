package br.com.oparoquiano.app.Dominio.Entidades;

/**
 * Created by luis on 10/01/18.
 */

public class IntecoesMissa {
    public static String nomeTabela = "tb_intecoes_missa";

    private String nome;
    private String paroquia;
    private String intencao;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getParoquia() {
        return paroquia;
    }

    public void setParoquia(String paroquia) {
        this.paroquia = paroquia;
    }

    public String getIntencao() {
        return intencao;
    }

    public void setIntencao(String intencao) {
        this.intencao = intencao;
    }
}
