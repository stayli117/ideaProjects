package net.people.jav;

import jdk.nashorn.api.scripting.JSObject;

import java.util.Date;

public class JBlock {
    public String hash;
    public String previousHash;
    private String data; //our data will be a simple message.
    private long timeStamp; //as number of milliseconds since 1/1/1970.

    //Block Constructor.
    public JBlock(String data, String previousHash) {
        this.data = data;
        this.previousHash = previousHash;
        this.timeStamp = new Date().getTime();
        hash = calculateHash();
    }

    public String calculateHash() {
        return JStringUtil.applySha256(
                previousHash +
                        Long.toString(timeStamp) +
                        data
        );
    }

    @Override
    public String toString() {

        return "hash :" + hash + "previousHash :" + previousHash + "data :" + data + "timeStamp :" + timeStamp;
    }
}
