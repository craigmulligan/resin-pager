# resin-pager
Integrate resin.io with PagerDuty to notify you when your device falls offline.

## How it works
Made use of Heroku's job scheduler to poll resin.io's API for an app's devices every 10 minutes. If a device is offline it will log an incident on PagerDuty by the Resin Device ID, providing a timestamp of when it was last online and a link to the device logs on resin.io.


## To Run

```
git clone https://github.com/craig-mulligan/resin-pager && cd resin-pager
```

```
heroku login
```

```
heroku create
```

```
git push heroku master
```

### Sign-up with [Pager-Duty](https://www.pagerduty.com/)
Grab the service key and set it as a heroku envar

```
heroku config:set PD_SERVICE_KEY=your_service_key
```

### [Resin.io Dashboard](https://dashboard.resin.io)
Grab your json web token from the preference page and set as a heroku envar
```
heroku config:set RESIN_JWT=your_JWT
```

Grab the app id of the app you'd like to monitor(find in url)
https://dashboard.resin.io/dashboard/apps/1463
```
heroku config:set RESIN_APP_ID=1463
```

### Add scheduler 

```
heroku addons:create scheduler
```

```
heroku addons:open scheduler
```

The command will take you to Heroku’s Scheduler where you can configure
the app. Name it “worker,” and set the frequency to “every 10 minutes.” Hit save.