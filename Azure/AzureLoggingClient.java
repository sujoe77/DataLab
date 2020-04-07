package com.sxp.logging.core.log4j.extensions.appender;

import com.sxp.java.fintranscom.rest.client.RestServiceHelper;
import com.sxp.java.fintranscom.rest.entity.rest.RestContext;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.lang3.time.DateFormatUtils;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class AzureLoggingClient {
    private static final String HMAC_SHA256_ALG = "HmacSHA256";

    private final String timeZone;
    private final String workspaceId;
    private final String workspaceKey;
    private final String logName;
    private final String timeStampField;

    public static void main(String[] args) {
        String message = "{\"class_name\":\"com.sxp.logging.core.LogObjectContainer\",\"class_version\":\"1.1.0\",\"level\":\"TRACE\",\"timestamp\":\"2020-04-06T00:00:656Z\",\"user_id\":\"saxo_payments\",\"application_id\":\"test_azure_logging_rest\",\"request_id\":\"503753831:520418641:1586131244655\",\"session_id\":\"ae9931b4-9168-4b12-be23-7b61e001053f\",\"server\":\"wls2vm\",\"wls_name\":\"SWUBS-external\",\"thread_name\":\"pool-29-thread-1\",\"os_name\":\"Linux\",\"os_arch\":\"amd64\",\"os_version\":\"4.14.35-1902.300.11.el7uek.x86_64\",\"jvm_mode\":\"mixed mode\",\"jvm_name\":\"Java(TM) SE Runtime Environment\",\"jvm_version\":\"1.8.0_171-b11\",\"session_state\":\"ACTIVE\",\"session_start\":\"2020-04-06T00:00:655Z\",\"session_touched\":\"2020-04-06T00:00:655Z\",\"logger\":\"com.sxp.dao.aspect.SqlLogger\",\"method\":\"ajc$before$com_sxp_dao_aspect_SqlLogger$1$f1b9b9cc\",\"line\":\"22\",\"message_id\":\"\",\"message_text\":\"SQL: SELECT mdmi.dcn,(select message from dual) message,mdmi.branch FROM FCUBS.MSTB_DLY_MSG_IN mdmi JOIN FCUBS.STTM_BRANCH sttm on mdmi.BRANCH = sttm.BRANCH_CODE WHERE mdmi.SWIFT_MSG_TYPE = '300' AND mdmi.MESSAGE IS NOT NULL AND sttm.END_OF_INPUT ='N' AND mdmi.DCN NOT IN (SELECT IMB_DCN FROM SAXOTRADER.MT300_MAPPING) and mdmi.MAKER_DT_STAMP >=sysdate-14 ORDER BY mdmi.MAKER_DT_STAMP DESC\\nCaller: com.sxp.dao.AOracleDAO->executeQuery\"}";
//        message = "{\"key\": 2}";
        System.out.println(message);
        AzureLoggingClient client = new AzureLoggingClient("63e53a41-bed0-482c-addb-2b707a30d89b",
                "WEAlLhLtlh70b+xxxxxxx==",
                "tracelog_json_CL",
                "timestamp",
                "GMT");
        client.sendLog(message);
    }

    public AzureLoggingClient(String workspaceId, String workspaceKey, String logName, String timeStampField, String timeZone) {
        this.workspaceId = workspaceId;
        this.workspaceKey = workspaceKey;
        this.logName = logName;
        this.timeStampField = timeStampField;
        this.timeZone = timeZone;
    }

    public void sendLog(String message) {
        String dateString = getDateString();
        byte[] jsonBytes = message.getBytes(StandardCharsets.US_ASCII);
        String hashedString = buildSignature(jsonBytes, dateString, workspaceKey);
        String signature = "SharedKey " + workspaceId + ":" + hashedString;
        postData(signature, dateString, message);
    }

    public String buildSignature(byte[] jsonBytes, String dateString, String key) {
        try {
            String signatureToHash = "POST\n" + jsonBytes.length + "\napplication/json\n" + "x-ms-date:" + dateString + "\n/api/logs";
            Mac sha256_HMAC = Mac.getInstance(HMAC_SHA256_ALG);
            byte[] bytes = Base64.decodeBase64(key);
            SecretKeySpec secret_key = new SecretKeySpec(bytes, HMAC_SHA256_ALG);
            sha256_HMAC.init(secret_key);
            byte[] encrypted = sha256_HMAC.doFinal(signatureToHash.getBytes());
            //printBytes(encrypted);
            return Base64.encodeBase64String(encrypted);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    private String getDateString() {
        TimeZone.setDefault(TimeZone.getTimeZone(timeZone));
        Calendar cal = Calendar.getInstance(TimeZone.getDefault());
        Date dateGMT = cal.getTime();
        return DateFormatUtils.format(dateGMT, "EEE, dd MMM yyyy HH:mm:ss z", Locale.US);
    }

    public void postData(final String signature, final String date, String json) {
        String url = "https://" + workspaceId + ".ods.opinsights.azure.com/api/logs?api-version=2016-04-01";
        RestContext<String, String> context = new RestContext(url);
        context.setHeaders(new HashMap<String, String>() {{
            put("Accept", "application/json");
            put("Log-Type", logName);
            put("Authorization", signature);
            put("x-ms-date", date);
            put("time-generated-field", timeStampField);
            put("content-type", "application/json");
        }});
        context.method("POST");
        context.requestEntity(json);
        RestServiceHelper.getInstance().getRestResponse(context);
    }
}
