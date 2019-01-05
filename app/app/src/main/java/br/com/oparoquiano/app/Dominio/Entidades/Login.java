package br.com.oparoquiano.app.Dominio.Entidades;

/**
 * Created by luis on 02/05/16.
 */
public class Login {
    private Integer lgn_id;
    private String lgn_email;
    private String lgn_senha;
    private String lgn_hash;

    public Integer getLgn_id() {
        return lgn_id;
    }

    public void setLgn_id(Integer lgn_id) {
        this.lgn_id = lgn_id;
    }

    public String getLgn_email() {
        return lgn_email;
    }

    public void setLgn_email(String lgn_email) {
        this.lgn_email = lgn_email;
    }

    public String getLgn_senha() {
        return lgn_senha;
    }

    public void setLgn_senha(String lgn_senha) {
        this.lgn_senha = lgn_senha;
    }

    public String getLgn_hash() {
        return lgn_hash;
    }

    public void setLgn_hash(String lgn_hash) {
        this.lgn_hash = lgn_hash;
    }
}
