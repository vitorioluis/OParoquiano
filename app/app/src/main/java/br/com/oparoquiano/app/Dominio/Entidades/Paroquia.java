package br.com.oparoquiano.app.Dominio.Entidades;

/**
 * Created by luis.vitorio on 13/03/2016.
 */
public class Paroquia {
    public static String nomeTabela = "tb_paroquia";


    private int par_id;
    private String dio_name;
    private String par_nome;
    private String par_site;
    private String par_num;
    private String par_cep;
    private String par_cidade;
    private String par_propaganda;
    private String par_logo;
    private String par_endereco;
    private Boolean par_fav;

    public String getPar_id() {
        return Integer.toString(par_id);
    }

    public void setPar_id(String par_id) {
        if (par_id == "null") {
            this.par_id = 0;
        } else {
            this.par_id = Integer.parseInt(par_id);
        }
    }

    public String getDio_name() {
        return dio_name;
    }

    public void setDio_name(String dio_name) {
        this.dio_name = dio_name;
    }


    public String getPar_nome() {
        return par_nome;
    }

    public void setPar_nome(String par_nome) {
        this.par_nome = par_nome;
    }


    public String getPar_site() {
        return par_site;
    }

    public void setPar_site(String par_site) {
        this.par_site = par_site;
    }

    public String getPar_num() {
        return par_num;
    }

    public void setPar_num(String par_num) {
        this.par_num = par_num;
    }

    public String getPar_cep() {
        return par_cep;
    }

    public void setPar_cep(String par_cep) {
        this.par_cep = par_cep;
    }

    public String getPar_cidade() {
        return par_cidade;
    }

    public void setPar_cidade(String par_cidade) {
        this.par_cidade = par_cidade;
    }

    public String getPar_propaganda() {
        return par_propaganda;
    }

    public void setPar_propaganda(String par_propaganda) {
        this.par_propaganda = par_propaganda;
    }

    public String getPar_logo() {
        return par_logo;
    }

    public void setPar_logo(String par_logo) {
        this.par_logo = par_logo;
    }

    public String getPar_endereco() {
        return par_endereco;
    }

    public void setPar_endereco(String par_endereco) {
        this.par_endereco = par_endereco;
    }

    public Boolean getPar_fav() {
        return par_fav;
    }

    public void setPar_fav(Boolean par_fav) {
        this.par_fav = par_fav;
    }
}
