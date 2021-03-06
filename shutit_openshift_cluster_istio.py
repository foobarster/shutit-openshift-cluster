def install_istio(s):

	# From: https://blog.openshift.com/evaluate-istio-openshift/?sc_cid=7016000000127iCAAQ

	s.send('oc new-project istio-system')
	s.send('oc project istio-system')
	s.send('oc adm policy add-scc-to-user anyuid -z istio-ingress-service-account')
	s.send('oc adm policy add-scc-to-user privileged -z istio-ingress-service-account')
	s.send('oc adm policy add-scc-to-user anyuid -z istio-egress-service-account')
	s.send('oc adm policy add-scc-to-user privileged -z istio-egress-service-account')
	s.send('oc adm policy add-scc-to-user anyuid -z istio-pilot-service-account')
	s.send('oc adm policy add-scc-to-user privileged -z istio-pilot-service-account')
	s.send('oc adm policy add-scc-to-user anyuid -z default')
	s.send('oc adm policy add-scc-to-user privileged -z default')
	s.send('oc adm policy add-cluster-role-to-user cluster-admin -z default')
	s.send('')
	s.send('curl -L https://git.io/getLatestIstio | sh -')
	s.send('ISTIO=`ls | grep istio`')
	s.send('export PATH="$PATH:~/$ISTIO/bin"')
	s.send('cd $ISTIO')
	s.send('oc apply -f install/kubernetes/istio.yaml')
	s.send('')
	s.send('oc create -f install/kubernetes/addons/prometheus.yaml')
	s.send('oc create -f install/kubernetes/addons/grafana.yaml')
	s.send('oc create -f install/kubernetes/addons/servicegraph.yaml')
	s.send('oc create -f install/kubernetes/addons/zipkin.yaml')
	s.send('oc expose svc grafana')
	s.send('oc expose svc servicegraph')
	s.send('oc expose svc zipkin')
	s.send('''SERVICEGRAPH=$(oc get route servicegraph -o jsonpath='{.spec.host}{"\n"}')/dotviz''')
	s.send('''GRAFANA=$(oc get route grafana -o jsonpath='{.spec.host}{"\n"}')''')
	s.send('''ZIPKIN=$(oc get route zipkin -o jsonpath='{.spec.host}{"\n"}')''')

	s.send('oc apply -f <(istioctl kube-inject -f samples/bookinfo/kube/bookinfo.yaml')
	s.send('oc expose svc productpage')
	s.send('''PRODUCTPAGE=$(oc get route productpage -o jsonpath='{.spec.host}{"\n"}''')
	s.send('watch -n 1 curl -o /dev/null -s -w %{http_code}\n $PRODUCTPAGE/productpage')

	# Check everything is up
	s.send('oc get pods')

	# Intelligent routing
	# TODO: git clone
	s.send('oc create -f samples/bookinfo/kube/route-rule-all-v1.yaml')
	s.send('oc create -f samples/bookinfo/kube/route-rule-reviews-test-v2.yaml')

#oc get routerule -o yaml

	# Delays
	s.send('oc create -f samples/bookinfo/kube/route-rule-ratings-test-delay.yaml')

	# Weight-based version routing
	s.send('oc replace -f samples/bookinfo/kube/route-rule-reviews-50-v3.yaml')

	# Quotas
	s.send('oc create -f samples/bookinfo/kube/mixer-rule-ratings-ratelimit.yaml')

	# Access control
	s.send('sed -i "s/istio-config-default/istio-system/g" samples/bookinfo/kube/mixer-rule-ratings-denial.yaml')
	s.send('oc create -f -f samples/bookinfo/kube/mixer-rule-ratings-denial.yaml')
