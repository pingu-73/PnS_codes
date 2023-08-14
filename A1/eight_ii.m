dic = containers.Map({'A', 'B', 'C', 'D', 'E'}, {{'B', 'D'}, {'A', 'C', 'D'}, {'B', 'E'}, {'A', 'B', 'E'}, {'C', 'D'}});
lis = {'A', 'B', 'C', 'D', 'E'};
count = containers.Map({'A', 'B', 'C', 'D', 'E'}, {0, 0, 0, 0, 0});

for i = 1:1000
    prev = lis{randi(length(lis))};
    for j = 1:20
        possible_choices = dic(prev);
        cur = possible_choices{randi(length(possible_choices))};
        count(cur) = count(cur) + 1;
        prev = cur;
    end
end

list1 = zeros(1, length(dic));
for i = 1:length(dic)
    list1(i) = count(lis{i});
end

list2 = sort(list1, 'descend');

node_list = cell(1, length(list2));
for i = 1:length(list2)
    for j = 1:length(lis)
        if count(lis{j}) == list2(i)
            disp([lis{j}, ' ', num2str(list2(i))]);
            node_list{i} = lis{j};
        end
    end
end

node_list = node_list(~cellfun('isempty', node_list));

bar(list2);
xticks(1:length(node_list));
xticklabels(node_list);
xlabel('Nodes');
ylabel('No of times Nodes is visited');
