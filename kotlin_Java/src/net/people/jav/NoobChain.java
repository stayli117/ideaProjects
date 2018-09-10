package net.people.jav;

import com.google.gson.Gson;

import java.util.ArrayList;

public class NoobChain {

    public static ArrayList<JBlock> blockchain = new ArrayList<JBlock>();

    public static void main(String[] args) {

        blockchain.add(new JBlock("Hi im the first block", "0"));
        blockchain.add(new JBlock("Yo im the second block", blockchain.get(blockchain.size() - 1).hash));
        blockchain.add(new JBlock("Hey im the third block", blockchain.get(blockchain.size() - 1).hash));

        Gson gson = new Gson();
        String json = gson.toJson(blockchain);
        System.out.println(json);
    }
}
