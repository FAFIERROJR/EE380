clear all
N = 5000
x = rand(1,N);
bins = [-1.00:.1:00];
[yvalues, xvalues] = hist(x,bins)
bar(xvalues, yvalues);
axis([-1.5 1.5 0 6000])
