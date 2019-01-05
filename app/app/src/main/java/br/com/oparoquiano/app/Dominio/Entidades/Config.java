package br.com.oparoquiano.app.Dominio.Entidades;

/**
 * Created by luis on 19/06/17.
 */

public class Config {
    public static String nomeTabela = "tb_config";
    private String cfg_desc;
    private int cfg_valor;

    public String getCfg_desc() {
        return cfg_desc;
    }

    public void setCfg_desc(String cfg_desc) {
        this.cfg_desc = cfg_desc;
    }

    public int getCfg_valor() {
        return cfg_valor;
    }

    public void setCfg_valor(int cfg_valor) {
        this.cfg_valor = cfg_valor;
    }
}
