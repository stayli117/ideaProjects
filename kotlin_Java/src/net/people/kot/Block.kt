package net.people.kot

import java.util.*
import java.lang.Long


class Block constructor(data: String, previousHash: String) {


    var mPreviousHash = previousHash
    var mData = data
    val mTimeStamp = Date().time
    var mHash = calculateHash();

    fun calculateHash(): String {
        return applySha256(
                mPreviousHash +
                        Long.toString(mTimeStamp)+
                        mData
        )
    }
}