from config import DB_PREFIX

class Semantics:
    query = None

    def __init__(self, query):
        self.query = query

    def query_treatment(self):
        querys = []
        joycons = []
        if "hash" in self.query:
            squery = self.query
            squery = squery.replace(',', ' ')
            query_splitted = squery.split()
            query_size = len(query_splitted)
            for i in range(0, query_size):
                if "select" in query_splitted[i] or "SELECT" in query_splitted[i] or "Select" in query_splitted[i]:
                    if "where" in self.query or "Where" in self.query or "WHERE" in self.query:
                        querys.extend(self.hashsplit_filtered(i, query_size, query_splitted))
                        joycons = self.join_conditions(i, query_size, query_splitted)
                        return querys, joycons
                    else:
                        querys.extend(self._hashsplit_nofilter(i, query_size, query_splitted, querys))
                        joycons.extend(self.join_conditions(i, query_size, query_splitted))
                        return querys, joycons
        else:
            querys.append("1")
            joycons = [None, None]
            return querys, joycons

    def _hashsplit_nofilter(self, i, query_size, query_splitted, results):
        nation_query = query_splitted[i]
        nflag = 0
        customer_query = query_splitted[i]
        cflag = 0
        lineitem_query = query_splitted[i]
        lflag = 0
        orders_query = query_splitted[i]
        oflag = 0
        part_query = query_splitted[i]
        pflag = 0
        partsupp_query = query_splitted[i]
        psflag = 0
        region_query = query_splitted[i]
        rflag = 0
        supplier_query = query_splitted[i]
        sflag = 0
        for j in range(i, query_size):
            if 'from' in query_splitted[j] or "FROM" in query_splitted[j] or "From" in query_splitted[j]:
                nation_query += ' ' + "from %s.NATION" % (DB_PREFIX)
                supplier_query += ' ' + "from %s.SUPPLIER" % (DB_PREFIX)
                customer_query += ' ' + "from %s.CUSTOMER" % (DB_PREFIX)
                lineitem_query += ' ' + "from %s.LINEITEM" % (DB_PREFIX)
                orders_query += ' ' + "from %s.ORDERS" % (DB_PREFIX)
                part_query += ' ' + "from %s.PART" % (DB_PREFIX)
                partsupp_query += ' ' + "from %s.PARTSUPP" % (DB_PREFIX)
                region_query += ' ' + "from %s.REGION" % (DB_PREFIX)
                if nflag != 0:
                    results.append(nation_query)
                if sflag != 0:
                    results.append(supplier_query)
                if cflag != 0:
                    results.append(customer_query)
                if lflag != 0:
                    results.append(lineitem_query)
                if oflag != 0:
                    results.append(orders_query)
                if pflag != 0:
                    results.append(part_query)
                if psflag != 0:
                    results.append(partsupp_query)
                if rflag != 0:
                    results.append(region_query)
                return results

            if "N_" in query_splitted[j]:
                if nflag >= 1:
                    nation_query += ',' + ' ' + query_splitted[j]
                else:
                    nation_query += ' ' + query_splitted[j]
                nflag += 1

            if "S_" in query_splitted[j] and "PS_" not in query_splitted[j]:
                if sflag >= 1:
                    supplier_query += ',' + ' ' + query_splitted[j]
                else:
                    supplier_query += ' ' + query_splitted[j]
                sflag += 1

            if "C_" in query_splitted[j]:
                if cflag >= 1:
                    customer_query += ',' + ' ' + query_splitted[j]
                else:
                    customer_query += ' ' + query_splitted[j]
                cflag += 1

            if "L_" in query_splitted[j]:
                if lflag >= 1:
                    lineitem_query += ',' + ' ' + query_splitted[j]
                else:
                    lineitem_query += ' ' + query_splitted[j]
                lflag += 1

            if "O_" in query_splitted[j]:
                if oflag >= 1:
                    orders_query += ',' + ' ' + query_splitted[j]
                else:
                    orders_query += ' ' + query_splitted[j]
                oflag += 1

            if "P_" in query_splitted[j] and "PS_" not in query_splitted[j]:
                if pflag >= 1:
                    part_query += ',' + ' ' + query_splitted[j]
                else:
                    part_query += ' ' + query_splitted[j]
                pflag += 1

            if "PS_" in query_splitted[j]:
                if psflag >= 1:
                    partsupp_query += ',' + ' ' + query_splitted[j]
                else:
                    partsupp_query += ' ' + query_splitted[j]
                psflag += 1

            if "R_" in query_splitted[j]:
                if rflag >= 1:
                    region_query += ',' + ' ' + query_splitted[j]
                else:
                    region_query += ' ' + query_splitted[j]
                rflag += 1

    def hashsplit_filtered(self, i, query_size, query_splitted):
        results = []
        nation_query = query_splitted[i]
        nflag = 0
        customer_query = query_splitted[i]
        cflag = 0
        lineitem_query = query_splitted[i]
        lflag = 0
        orders_query = query_splitted[i]
        oflag = 0
        part_query = query_splitted[i]
        pflag = 0
        partsupp_query = query_splitted[i]
        psflag = 0
        region_query = query_splitted[i]
        rflag = 0
        supplier_query = query_splitted[i]
        sflag = 0
        ncounter = 0
        scounter = 0
        ccounter = 0
        lcounter = 0
        ocounter = 0
        pcounter = 0
        pscounter = 0
        rcounter = 0
        wstring = ""
        fstring = ""

        for j in range(i, query_size):
            if "N_" in query_splitted[j] and "=" not in query_splitted[j]:
                if nflag >= 1:
                    nation_query += ',' + ' ' + query_splitted[j]
                else:
                    nation_query += ' ' + query_splitted[j]
                nflag += 1

            if "S_" in query_splitted[j] and "PS_" not in query_splitted[j] and "=" not in \
                    query_splitted[
                        j]:
                if sflag >= 1:
                    supplier_query += ',' + ' ' + query_splitted[j]
                else:
                    supplier_query += ' ' + query_splitted[j]
                sflag += 1

            if "C_" in query_splitted[j and "=" not in query_splitted[j]]:
                if cflag >= 1:
                    customer_query += ',' + ' ' + query_splitted[j]
                else:
                    customer_query += ' ' + query_splitted[j]
                cflag += 1

            if "L_" in query_splitted[j] and "=" not in query_splitted[j]:
                if lflag >= 1:
                    lineitem_query += ',' + ' ' + query_splitted[j]
                else:
                    lineitem_query += ' ' + query_splitted[j]
                lflag += 1

            if "O_" in query_splitted[j] and "=" not in query_splitted[j]:
                if oflag >= 1:
                    orders_query += ',' + ' ' + query_splitted[j]
                else:
                    orders_query += ' ' + query_splitted[j]
                oflag += 1

            if "P_" in query_splitted[j] and "PS_" not in query_splitted[j] and "=" not in \
                    query_splitted[
                        j]:
                if pflag >= 1:
                    part_query += ',' + ' ' + query_splitted[j]
                else:
                    part_query += ' ' + query_splitted[j]
                pflag += 1

            if "PS_" in query_splitted[j and "=" not in query_splitted[j]]:
                if psflag >= 1:
                    partsupp_query += ',' + ' ' + query_splitted[j]
                else:
                    partsupp_query += ' ' + query_splitted[j]
                psflag += 1

            if "R_" in query_splitted[j] and "=" not in query_splitted[j]:
                if rflag >= 1:
                    region_query += ',' + ' ' + query_splitted[j]
                else:
                    region_query += ' ' + query_splitted[j]
                rflag += 1

            if query_splitted[j] == "where" or query_splitted[j] == "WHERE" or query_splitted[j] == "Where" or query_splitted[j] == "ORDER":

                for k in range(j, query_size+1):
                    if ";" in query_splitted[k-1]:
                        fstring += " " + "from"
                        if ncounter != 0 or scounter != 0 or ccounter != 0 or lcounter != 0 or ocounter != 0 or pcounter != 0 or pscounter != 0 or rcounter != 0:
                            counters = [ncounter, scounter, ccounter, lcounter, ocounter, pcounter, pscounter, rcounter]
                            for c in range(0, len(counters)):
                                if counters[c] != 0 and c == 0:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.NATION" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.NATION" % (DB_PREFIX)
                                if counters[c] != 0 and c == 1:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.SUPPLIER" % (DB_PREFIX)
                                    else:
                                        fstring += ' loop' + "%s.SUPPLIER" % (DB_PREFIX)
                                if counters[c] != 0 and c == 2:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.CUSTOMER" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.CUSTOMER" % (DB_PREFIX)
                                if counters[c] != 0 and c == 3:
                                    if "TPC" in lineitem_query:
                                        fstring += ', ' + "%s.LINEITEM" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.LINEITEM" % (DB_PREFIX)
                                if counters[c] != 0 and c == 4:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.ORDERS" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.ORDERS" % (DB_PREFIX)
                                if counters[c] != 0 and c == 5:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.PART" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.PART" % (DB_PREFIX)
                                if counters[c] != 0 and c == 6:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.PARTSUPP" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.PARTSUPP" % (DB_PREFIX)
                                if counters[c] != 0 and c == 7:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.REGION" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.REGION" % (DB_PREFIX)

                            if "NATION" in fstring:
                                nation_query += fstring + wstring
                            else:
                                nation_query += " from %s.NATION" % (DB_PREFIX)
                            if "SUPPLIER" in fstring:
                                supplier_query += fstring + wstring
                            else:
                                supplier_query += " from %s.SUPPLIER" % (DB_PREFIX)
                            if "CUSTOMER" in fstring:
                                customer_query += fstring + wstring
                            else:
                                customer_query += " from %s.CUSTOMER" % (DB_PREFIX)
                            if "LINEITEM" in fstring:
                                lineitem_query += fstring + wstring
                            else:
                                lineitem_query += " from %s.LINEITEM" % (DB_PREFIX)
                            if "ORDERS" in fstring:
                                orders_query += fstring + wstring
                            else:
                                orders_query += " from %s.ORDERS" % (DB_PREFIX)
                            if "PART" in fstring:
                                part_query += fstring + wstring
                            else:
                                part_query += " from %s.PART" % (DB_PREFIX)
                            if "PARTSUPP" in fstring:
                                partsupp_query += fstring + wstring
                            else:
                                partsupp_query += " from %s.PARTSUPP" % (DB_PREFIX)
                            if "REGION" in fstring:
                                region_query += fstring + wstring
                            else:
                                region_query += " from TPCSOUCE.REGION"
                            print(query_splitted[query_size - 1])
                            print(nation_query)
                            print(supplier_query)
                        if nflag != 0:
                            results.append(nation_query)
                        if sflag != 0:
                            results.append(supplier_query)
                        if cflag != 0:
                            results.append(customer_query)
                        if lflag != 0:
                            results.append(lineitem_query)
                        if oflag != 0:
                            results.append(orders_query)
                        if pflag != 0:
                            results.append(part_query)
                        if psflag != 0:
                            results.append(partsupp_query)
                        if rflag != 0:
                            results.append(region_query)
                        return results
                    if query_splitted[k-1] == query_splitted[query_size-1]:
                        fstring += " " + "from"
                        if ncounter != 0 or scounter != 0 or ccounter != 0 or lcounter != 0 or ocounter != 0 or pcounter != 0 or pscounter != 0 or rcounter != 0:
                            counters = [ncounter, scounter, ccounter, lcounter, ocounter, pcounter, pscounter, rcounter]
                            for c in range(0, len(counters)):
                                if counters[c] != 0 and c == 0:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.NATION" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.NATION" % (DB_PREFIX)
                                if counters[c] != 0 and c == 1:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.SUPPLIER" % (DB_PREFIX)
                                    else:
                                        fstring += ' loop' + "%s.SUPPLIER" % (DB_PREFIX)
                                if counters[c] != 0 and c == 2:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.CUSTOMER" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.CUSTOMER" % (DB_PREFIX)
                                if counters[c] != 0 and c == 3:
                                    if "TPC" in lineitem_query:
                                        fstring += ', ' + "%s.LINEITEM" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.LINEITEM" % (DB_PREFIX)
                                if counters[c] != 0 and c == 4:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.ORDERS" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.ORDERS" % (DB_PREFIX)
                                if counters[c] != 0 and c == 5:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.PART" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.PART" % (DB_PREFIX)
                                if counters[c] != 0 and c == 6:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.PARTSUPP" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.PARTSUPP" % (DB_PREFIX)
                                if counters[c] != 0 and c == 7:
                                    if "TPC" in fstring:
                                        fstring += ', ' + "%s.REGION" % (DB_PREFIX)
                                    else:
                                        fstring += ' ' + "%s.REGION" % (DB_PREFIX)

                            if "NATION" in fstring:
                                nation_query += fstring + wstring
                            else:
                                nation_query += " from %s.NATION" % (DB_PREFIX)
                            if "SUPPLIER" in fstring:
                                supplier_query += fstring + wstring
                            else:
                                supplier_query += " from %s.SUPPLIER" % (DB_PREFIX)
                            if "CUSTOMER" in fstring:
                                customer_query += fstring + wstring
                            else:
                                customer_query += " from %s.CUSTOMER" % (DB_PREFIX)
                            if "LINEITEM" in fstring:
                                lineitem_query += fstring + wstring
                            else:
                                lineitem_query += " from %s.LINEITEM" % (DB_PREFIX)
                            if "ORDERS" in fstring:
                                orders_query += fstring + wstring
                            else:
                                orders_query += " from %s.ORDERS" % (DB_PREFIX)
                            if "PART" in fstring:
                                part_query += fstring + wstring
                            else:
                                part_query += " from %s.PART" % (DB_PREFIX)
                            if "PARTSUPP" in fstring:
                                partsupp_query += fstring + wstring
                            else:
                                partsupp_query += " from %s.PARTSUPP" % (DB_PREFIX)
                            if "REGION" in fstring:
                                region_query += fstring + wstring
                            else:
                                region_query += " from TPCSOUCE.REGION"
                            if nflag != 0:
                                results.append(nation_query)
                            if sflag != 0:
                                results.append(supplier_query)
                            if cflag != 0:
                                results.append(customer_query)
                            if lflag != 0:
                                results.append(lineitem_query)
                            if oflag != 0:
                                results.append(orders_query)
                            if pflag != 0:
                                results.append(part_query)
                            if psflag != 0:
                                results.append(partsupp_query)
                            if rflag != 0:
                                results.append(region_query)
                            print(supplier_query)
                            return results
                    wstring += str(' ' + query_splitted[k])
                    if "N_" in query_splitted[k]:
                        ncounter += 1
                    if "S_" in query_splitted[k] and "PS_" not in query_splitted[k]:
                        scounter += 1
                    if "C_" in query_splitted[k]:
                        ccounter += 1
                    if "L_" in query_splitted[k]:
                        lcounter += 1
                    if "O_" in query_splitted[k]:
                        ocounter += 1
                    if "P_" in query_splitted[k] and "PS_" not in query_splitted[k]:
                        pcounter += 1
                    if "PS_" in query_splitted[k]:
                        pscounter += 1
                    if "R_" in query_splitted[k]:
                        rcounter += 1

    def join_conditions(self, i, query_size, query_splitted):
        leftcon = list()
        rightcon = list()
        for j in range(i, query_size):
            if query_splitted[j] == "on":
                conditions = query_splitted[j+1].split('=')
                leftcon.append(conditions[0])
                rightcon.append(conditions[1])
        return leftcon, rightcon









