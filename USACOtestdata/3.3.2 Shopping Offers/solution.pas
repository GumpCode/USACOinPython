{
ID: asiapea1
PROG: shopping
LANG: PASCAL
}
program shopping;
var
  hao{Ψһ���},cast{ֱ�ӹ���Ļ���}:array[1..5] of integer;
  mm{ĳ��ƷҪ�����}:array[1..5] of byte;
  y{�Żݼ۸�}:array[1..100] of integer;
  f:array[0..5,0..5,0..5,0..5,0..5] of integer;
  z{�Żݷ�ʽ}:array[1..100,1..5] of integer;
  i,j,m,n,k,b,s,xx,yy,i1,i2,i3,i4,i5:integer;
  key{����Żݻ᲻���򵽲�����Ķ���}:array[1..100] of boolean;
 
function w(nk:integer):byte;{����NK����ǵڼ�����Ʒ}
var
  i:integer;
begin
  for i:=1 to b do if nk=hao[i] then exit(i);
  w:=0;{�����������Ʒ}
end;
begin
assign(input,'shopping.in');
reset(input);
assign(output,'shopping.out');
rewrite(output);
  readln(m);
  for i:=1 to m do readln;{�����Żݷ�ʽ�Ķ�ȡ��}
  readln(b);
  for i:=1 to b do readln(hao[i],mm[i],cast[i]);
reset(input);{�ص��ļ���ͷ��ȡ�Żݷ�ʽ}
  readln(m);
  for i:=1 to m do
  begin
    read(n);
    for j:=1 to n do begin
      read(xx,yy);
      xx:=w(xx);
      if xx=0 then key[i]:=true;{�����Żݲ����á���}
      if not key[i] then z[i,xx]:=yy;
    end;
    readln(y[i]);
  end;
 
 
//��ʼ��Ϊ�����Ż�ʱ�Ĺ���۸�
  for i1:=0 to mm[1] do
    for i2:=0 to mm[2] do
      for i3:=0 to mm[3] do
        for i4:=0 to mm[4] do
          for i5:=0 to mm[5] do
            f[i1,i2,i3,i4,i5]:=i1*cast[1]+i2*cast[2]+i3*cast[3]+i4*cast[4]+i5*cast[5];
//��ʼ������
  for i:=1 to m do
  if not key[i] then
    for i1:=z[i,1] to mm[1] do
      for i2:=z[i,2] to mm[2] do
        for i3:=z[i,3] to mm[3] do
          for i4:=z[i,4] to mm[4] do
            for i5:=z[i,5] to mm[5] do
              if f[i1,i2,i3,i4,i5]>f[i1-z[i,1],i2-z[i,2],i3-z[i,3],i4-z[i,4],i5-z[i,5]]+y[i] then
                f[i1,i2,i3,i4,i5]:=f[i1-z[i,1],i2-z[i,2],i3-z[i,3],i4-z[i,4],i5-z[i,5]]+y[i];
  writeln(f[mm[1],mm[2],mm[3],mm[4],mm[5]]);
close(output);
end.