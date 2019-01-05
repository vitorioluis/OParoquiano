package br.com.oparoquiano.app.Util;

import android.app.Notification;
import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.graphics.BitmapFactory;
import android.media.Ringtone;
import android.media.RingtoneManager;
import android.net.Uri;
import android.support.v4.app.NotificationCompat;

import br.com.oparoquiano.app.R;

/**
 * Created by luis on 19/06/17.
 * Exemplo de uso:
 * <p>
 * String[] descs = new String[]{"Luis", "teste", "Bruna", "Descrição 4"};
 * Notificacoes nt = new Notificacoes();
 * nt.Notificacoes(actMain.this, descs);
 */

public class Notificacoes {


    public void Noticacacoes(Context context, String[] descs) {

        NotificationManager nm = (NotificationManager) context.getSystemService(context.NOTIFICATION_SERVICE);
        PendingIntent p = PendingIntent.getActivity(context, 0, new Intent(context, Notificacoes.class), 0);

        NotificationCompat.Builder builder = new NotificationCompat.Builder(context);
        builder.setTicker("Ticker Texto");
        builder.setContentTitle("OParoquiano");
        builder.setSmallIcon(R.drawable.icon_app);
        builder.setLargeIcon(BitmapFactory.decodeResource(context.getResources(), R.drawable.icon_app));
        builder.setContentIntent(p);

        NotificationCompat.InboxStyle style = new NotificationCompat.InboxStyle();

        for (int i = 0; i < descs.length; i++) {
            style.addLine(descs[i]);
        }
        builder.setStyle(style);

        Notification n = builder.build();
        n.vibrate = new long[]{150, 300, 150, 600};
        n.flags = Notification.FLAG_AUTO_CANCEL;
        nm.notify(R.drawable.icon_app, n);

        try {
            Uri som = RingtoneManager.getDefaultUri(RingtoneManager.TYPE_NOTIFICATION);
            Ringtone toque = RingtoneManager.getRingtone(context, som);
            toque.play();
        } catch (Exception e) {
        }
    }
}
