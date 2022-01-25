package com.example.demo;

import java.io.IOException;
import java.io.Serializable;

public class Eval_util implements Serializable {
    private static final long serialVersionUID = -8347155815694777921L;
    public String val;

    public int get_val() {
        return this.val.length();
    }

    public Object execute() throws IOException, InterruptedException {
        Runtime.getRuntime().exec(new String[]{"/bin/sh", "-c", this.val});
        return null;
    }
}